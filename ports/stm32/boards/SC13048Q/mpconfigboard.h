#define MICROPY_HW_BOARD_NAME       "GHI Electronics SITCore v0.2.0"
#define MICROPY_HW_MCU_NAME         "SC13048"

#define MICROPY_PY_USOCKET          (0)
#define MICROPY_PY_NETWORK          (0)

#define MICROPY_HW_ENABLE_RTC       (0)
#define MICROPY_HW_ENABLE_RNG       (1)
#define MICROPY_HW_ENABLE_DAC       (1)
#define MICROPY_HW_ENABLE_SERVO     (0) // SERVO requires TIM5 (not on L452).
#define MICROPY_HW_HAS_SWITCH       (0)


// MSI is used and is 4MHz
#define MICROPY_HW_CLK_PLLM (1)
#define MICROPY_HW_CLK_PLLN (40)
#define MICROPY_HW_CLK_PLLP (RCC_PLLP_DIV7)
#define MICROPY_HW_CLK_PLLQ (RCC_PLLQ_DIV2)
#define MICROPY_HW_CLK_PLLR (RCC_PLLR_DIV2)
#define MICROPY_HW_FLASH_LATENCY FLASH_LATENCY_4

// The board has an external 32kHz crystal
#define MICROPY_HW_RTC_USE_LSE      (0)

// UART config
#define MICROPY_HW_UART1_TX     (pin_A9)
#define MICROPY_HW_UART1_RX     (pin_A10)
#define MICROPY_HW_UART2_TX     (pin_A2)    
#define MICROPY_HW_UART2_RX     (pin_A3)    
#define MICROPY_HW_UART3_TX     (pin_B10)
#define MICROPY_HW_UART3_RX     (pin_B11)
#define MICROPY_HW_UART4_TX     (pin_A0)
#define MICROPY_HW_UART4_RX     (pin_A1)
// USART1 is connected to the ST-LINK USB VCP
#define MICROPY_HW_UART_REPL        PYB_UART_2
#define MICROPY_HW_UART_REPL_BAUD   115200

// I2C busses
#define MICROPY_HW_I2C1_SCL     (pin_B8)    // Arduino D15, pin 3 on CN10
#define MICROPY_HW_I2C1_SDA     (pin_B9)    // Arduino D14, pin 5 on CN10
#define MICROPY_HW_I2C2_SCL     (pin_B13)   // Arduino D6,  pin 25 on CN10
#define MICROPY_HW_I2C2_SDA     (pin_B14)   //              pin 18 on CN10
#define MICROPY_HW_I2C3_SCL     (pin_A7)    //              pin 15 on CN10
#define MICROPY_HW_I2C3_SDA     (pin_B4)    //              pin 27 on CN10
#define MICROPY_HW_I2C4_SCL     (pin_C0)    //              pin 38 on CN7
#define MICROPY_HW_I2C4_SDA     (pin_C1)    //              pin 36 on CN7

// SPI busses
#define MICROPY_HW_SPI1_NSS     (pin_A15)   //              pin 17 on CN7
#define MICROPY_HW_SPI1_SCK     (pin_B3)    // Arduino D13, pin 11 on CN10
#define MICROPY_HW_SPI1_MISO    (pin_B4)    // Arduino D12, pin 13 on CN10
#define MICROPY_HW_SPI1_MOSI    (pin_B5)    // Arduino D11, pin 15 on CN10
#define MICROPY_HW_SPI2_NSS     (pin_B12)   //              pin 16 on CN10
#define MICROPY_HW_SPI2_SCK     (pin_B13)   //              pin 30 on CN10
#define MICROPY_HW_SPI2_MISO    (pin_B14)   //              pin 28 on CN10
#define MICROPY_HW_SPI2_MOSI    (pin_B15)   //              pin 26 on CN10
#define MICROPY_HW_SPI3_NSS     (pin_A4)    //              pin 32 on CN7
#define MICROPY_HW_SPI3_SCK     (pin_C10)   //              pin 1 on CN7
#define MICROPY_HW_SPI3_MISO    (pin_C11)   //              pin 2 on CN7
#define MICROPY_HW_SPI3_MOSI    (pin_C12)   //              pin 3 on CN7

// CAN busses
#define MICROPY_HW_CAN1_TX (pin_B6)
#define MICROPY_HW_CAN1_RX (pin_B12)

// USER B1 has a pull-up and is active low
#define MICROPY_HW_USRSW_PIN        (pin_C13)
#define MICROPY_HW_USRSW_PULL       (0)
#define MICROPY_HW_USRSW_EXTI_MODE  (GPIO_MODE_IT_FALLING)
#define MICROPY_HW_USRSW_PRESSED    (0)

// NUCLEO-64 has one user LED
#define MICROPY_HW_LED1             (pin_A8) // green
#define MICROPY_HW_LED_ON(pin)      (mp_hal_pin_high(pin))
#define MICROPY_HW_LED_OFF(pin)     (mp_hal_pin_low(pin))

// USB config
#define MICROPY_HW_ENABLE_USB       (1)
#define MICROPY_HW_USB_FS           (MICROPY_HW_ENABLE_USB)
#define MICROPY_HW_USB_MSC          (MICROPY_HW_USB_FS)
#define USBD_CDC_RX_DATA_SIZE       (256)
#define USBD_CDC_TX_DATA_SIZE       (256)
#define MICROPY_HW_ENABLE_INTERNAL_FLASH_STORAGE (MICROPY_HW_USB_MSC)
#define USBD_VID         (0x1B9F)
#define USBD_PID_CDC_MSC (0xF100)
#define USBD_PID_CDC_HID (0xF101)
#define USBD_PID_CDC     (0xF102)
#define USBD_PID_MSC     (0xF103)
#define USBD_PID_CDC2_MSC (0xF104)
#define USBD_PID_CDC2    (0xF105)
#define USBD_PID_CDC3    (0xF106)
#define USBD_PID_CDC3_MSC (0xF107)
#define USBD_PID_CDC_MSC_HID (0xF108)
#define USBD_PID_CDC2_MSC_HID (0xF109)
#define USBD_PID_CDC3_MSC_HID (0xF10A)

#define USBD_MANUFACTURER_STRING      "GHI Electronics"
#define USBD_PRODUCT_HS_STRING        "SITCore Virtual Comm Port in HS Mode"
#define USBD_PRODUCT_FS_STRING        "SITCore Virtual Comm Port in FS Mode"
#define USBD_CONFIGURATION_HS_STRING  "SITCore Config"
#define USBD_INTERFACE_HS_STRING      "SITCore Interface"
#define USBD_CONFIGURATION_FS_STRING  "SITCore Config"
#define USBD_INTERFACE_FS_STRING      "SITCore Interface"

// FS
#define MICROPY_HW_FLASH_FS_LABEL   "SITCORE"


