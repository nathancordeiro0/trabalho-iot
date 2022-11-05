from machine import Pin, Timer
import utime
        
sensor_temperatura = machine.ADC(4)
conversor = 3.3 / (65535)

switch = Pin(4, Pin.IN)

while True:
  if switch.value() == 1:               # Switch posição 1 = Sprinkter ligado.
    led = Pin(1, Pin.OUT)
    led = Pin(2, Pin.OUT)
    led.off()

    led = Pin(3, Pin.OUT)
    led.on()
  else:
    leitura = sensor_temperatura.read_u16() * conversor
    temperatura = 27 - (leitura - 0.706)/0.001721
  
    print(f'Marcando no momento {temperatura:.2f}°C')
  
    if temperatura > 500 :               # Luz azul piscando temperatura amena. 
      led = Pin(3, Pin.OUT)
      led.off()

      led = Pin(1, Pin.OUT)
      led.toggle()
      utime.sleep(1)

    else:                                # Luz vermelha piscando temperatura perigosa para as plantas.
      led = Pin(3, Pin.OUT)
      led.off()

      led = Pin(2, Pin.OUT)
      led.toggle()
      utime.sleep(1)

