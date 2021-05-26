MCU_SERIES = l4
CMSIS_MCU = STM32L452xx
AF_FILE = boards/stm32l452_af.csv
LD_FILES = boards/SC13048Q/stm32l452re_bl.ld boards/common_bl.ld
TEXT0_ADDR = 0x08006400
OPENOCD_CONFIG = boards/openocd_stm32l4.cfg
