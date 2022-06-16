# Increase the number of requests accepted by nginx

exec { 'set limit to 6000':
  command => '/bin/sed -i "s/ULIMIT.*/ULIMIT=\"-n 6000\"/" /etc/default/nginx'
} -> exec { 'restart nginx':
  command => '/usr/sbin/service nginx restart',
}
