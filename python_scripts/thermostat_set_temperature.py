thermostat_id  = data.get('thermostat_id','')
temp  = data.get('temperature',None)
if thermostat_id != "" and temp is not None:
   thermostat = hass.states.get(thermostat_id)
   attributes = thermostat.attributes.copy()
   attributes['current_temperature'] = temp
   hass.states.set(thermostat_id, thermostat.state, attributes)
   logger.error("current_temperature has been set for {} to {}".format(thermostat_id,temp)  
else:
   logger.error("Wrong thermostat_id")