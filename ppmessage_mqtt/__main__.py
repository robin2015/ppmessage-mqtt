from ppmessage_mqtt import mqtt_server
from tornado.options import parse_command_line

if __name__ == "__main__":
    # initial tornado options (logging used)
    parse_command_line()
    mqtt_server()