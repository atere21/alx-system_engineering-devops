# 0-the_sky_is_the_limit_not.pp
exec { 'task-0':
  provider => 'shell',
  command  => "sed -i 's/15/1000/g' /etc/default/nginx; service nginx restart",
}
