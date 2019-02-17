sensor_id  = data.get('sensor')

if sensor_id != "":
   sensor = hass.states.get(sensor_id)
   temp = sensor.state
   logger.info("Temp: {}".format(temp))
else:
   logger.error("Wrong sensor id")