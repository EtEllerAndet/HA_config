thermostat_id  = data.get('thermostat_id','')
temp  = data.get('temperature',None)

logger.info("input {} : {}".format(thermostat_id,temp))
thermostat = hass.states.get(thermostat_id)

if thermostat is not None and temp is not None:
    attributes = thermostat.attributes.copy()
    attributes['current_temperature'] = temp
    hass.states.set(thermostat_id, thermostat.state, attributes)
    logger.info("current_temperature has been set for {} to {}".format(thermostat_id,temp))
else:
    logger.error("Wrong thermostat_id")