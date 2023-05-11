# issue on line 137 of /var/www/html/wp-settings.php
$rep = 'require_once( ABSPATH . WPINC . \'/class-wp-locale.php\' );'
$settings = '/var/www/html/wp-settings.php'
$cmd = "sed -i \"/class-wp-locale.phpp/c ${::rep}\" ${::settings}"
exec { 'serverfix':
  path    => '/bin',
  command => $cmd,
}
# Create a manifest that fixes file name typo
exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin/'
}
