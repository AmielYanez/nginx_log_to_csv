
COL_IP_ADDRESS = 'ip_address'
COL_LOG_TIME = 'log_time'
COL_LOG_PATH = 'log_path'
COL_LOG_STATUS = 'log_status'
COL_LOG_BW = 'log_bandwidth'
COL_LOG_REFERER = 'log_referer'
COL_USER_AGENT = 'user_agent'
COL_COUNTRY = 'country'
COL_STATE = 'state'
COL_DEVICE_TYPE = 'device_type'
COL_BROWSER = 'browser'


LINE_PATTERN = (r''
           '(\d+.\d+.\d+.\d+)\s-\s-\s' #IP address
           '\[(.+)\]\s' #datetime
           '"GET\s(.+)\s\w+/.+"\s' #requested file
           '(\d+)\s' #status
           '(\d+)\s' #bandwidth
           '"(.+)"\s' #referrer
           '"(.+)"' #user agent
                )