import re
import constants
from geoip import geolite2
from user_agents import parse as user_agent_parser


def read_file(f, chunk_size=2048):
    while True:
        line = f.read(chunk_size)
        if not line:
            break
        yield line


def parse_line(line):
    try:
        return re.findall(constants.LINE_PATTERN, line)[0]
    except Exception as e:
        return None


def find_ip_address_location(ip_address):
    result = {
        constants.COL_COUNTRY: "unknown",
        constants.COL_STATE: "unknown"
    }
    try:
        match = geolite2.lookup(ip_address)
    except:
        return result

    if not match:
        return result
    if match.country:
        result[constants.COL_COUNTRY] = match.country

    if match.subdivisions:
        result[constants.COL_STATE] = list(match.subdivisions)[0]

    return result


def parse_user_agent(user_agent):
    result = {
        constants.COL_DEVICE_TYPE: "unknown",
        constants.COL_BROWSER: "unknown"
    }
    try:
        user_agent_parsed = user_agent_parser(user_agent)
        if user_agent_parsed.is_pc:
            result[constants.COL_DEVICE_TYPE] = "Desktop"
        elif user_agent_parsed.is_tablet:
            result[constants.COL_DEVICE_TYPE] = "Tablet"
        elif user_agent_parsed.is_mobile:
            result[constants.COL_DEVICE_TYPE] = "Mobile"

        result[constants.COL_BROWSER] = user_agent_parsed.browser.family

    except:
        pass
    return result


def process_line(line):
    data = parse_line(line)

    if not data:
        return
    datum = dict()
    datum[constants.COL_IP_ADDRESS], \
    datum[constants.COL_LOG_TIME], \
    datum[constants.COL_LOG_PATH], \
    datum[constants.COL_LOG_STATUS], \
    datum[constants.COL_LOG_BW], \
    datum[constants.COL_LOG_REFERER], \
    datum[constants.COL_USER_AGENT] = data

    location_data = find_ip_address_location(datum[constants.COL_IP_ADDRESS])
    datum[constants.COL_COUNTRY] = location_data[constants.COL_COUNTRY]
    datum[constants.COL_STATE] = location_data[constants.COL_STATE]

    device_data = parse_user_agent(datum[constants.COL_USER_AGENT])
    datum[constants.COL_DEVICE_TYPE] = device_data[constants.COL_DEVICE_TYPE]
    datum[constants.COL_BROWSER] = device_data[constants.COL_BROWSER]

    return datum
