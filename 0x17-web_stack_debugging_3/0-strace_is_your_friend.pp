# Create a manifest that fixes why Apache is returning a 500 error
exec { 'fix_typo':
  command => 'mv /var/www/html/wp-includes/class-wp-locale.php /var/www/html/wp-includes/class-wp-locale.phpp',
  path    => '/bin/'
}
