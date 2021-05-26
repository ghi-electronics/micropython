// Original version from https://github.com/adafruit/Adafruit_NeoPixel
// Modifications by dpgeorge to support auto-CPU-frequency detection

// This is a mash-up of the Due show() code + insights from Michael Miller's
// ESP8266 work for the NeoPixelBus library: github.com/Makuna/NeoPixelBus
// Needs to be a separate .c file to enforce ICACHE_RAM_ATTR execution.

// Modification by GHI to support SC13048Q

#include "py/mpconfig.h"
#include "py/mphal.h"

#define TICK_ONE (64 - 16)
#define TICK_ZERO (28 - 16)
#define TICK_RESET (8000)

inline static void neopixel_send_reset(GPIO_TypeDef* port, uint32_t pinMask) {
    port->BSRR = pinMask << 16;

    uint32_t now = DWT->CYCCNT;

    while ((uint32_t)(DWT->CYCCNT - now) < TICK_RESET);

}

inline static void neopixel_send_one(GPIO_TypeDef* port, uint32_t pinMask) {
    port->BSRR = pinMask;

    uint32_t now = DWT->CYCCNT;

    while ((uint32_t)(DWT->CYCCNT - now) < TICK_ONE);

    port->BSRR = pinMask << 16;

    now = DWT->CYCCNT;

    while ((uint32_t)(DWT->CYCCNT - now) < TICK_ZERO - 1);
}

inline static void neopixel_send_zero(GPIO_TypeDef* port, uint32_t pinMask) {
    port->BSRR = pinMask;

    uint32_t now = DWT->CYCCNT;

    while ((uint32_t)(DWT->CYCCNT - now) < TICK_ZERO);

    port->BSRR = pinMask << 16;

    now = DWT->CYCCNT;

    while ((uint32_t)(DWT->CYCCNT - now) < TICK_ONE - 1);
}

void neopixel_write(uint8_t pin, uint8_t* pixels, uint32_t numBytes) {

    uint8_t pixel;
    uint32_t pinMask;
    uint32_t irqStatus;

    GPIO_TypeDef* port = (GPIO_TypeDef*)(GPIOA_BASE + ((pin >> 4) << 10));

    pinMask = 1 << (pin & 0x0F);

    mp_hal_ticks_cpu();
    irqStatus = __get_PRIMASK();

    __disable_irq();

    for (int n = 0; n < numBytes; n++) {
        pixel = pixels[n];
        for (int m = 7; m >= 0; m--) {
            if (pixel & (1 << m)) {
                neopixel_send_one(port, pinMask);
            }
            else {
                neopixel_send_zero(port, pinMask);
            }
        }

    }

    neopixel_send_reset(port, pinMask);

    if ((irqStatus & 1) == 0) {
        __enable_irq();
    }
}
