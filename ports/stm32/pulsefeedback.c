#include "py/mpconfig.h"
#include "py/mphal.h"

uint32_t pulsefeedback_read(mp_obj_t p) {
	uint32_t pulseValue = 1;
	uint32_t current = 0;	
	uint32_t timeLenght = 0;
	
	mp_hal_pin_obj_t pin = mp_hal_get_pin_obj(p);
	mp_hal_ticks_cpu();
		
	mp_hal_pin_output(pin);
	mp_hal_pin_write(pin, pulseValue);
	
	mp_hal_delay_us(10000);	
		
	uint32_t start = mp_hal_ticks_us();
	uint32_t end = start + 1000000;
	
	mp_hal_pin_config((pin), MP_HAL_PIN_MODE_INPUT, MP_HAL_PIN_PULL_DOWN, 0);
		
	while (1) {
		uint32_t now = mp_hal_ticks_us();
		
		current = mp_hal_pin_read(pin);
		
		if (current != pulseValue) {
			timeLenght = now - start;
			
			break;
		}
		
		if (now > end) {
			break;
		}	
	}		
	return timeLenght;	
}

