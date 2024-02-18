# Tint2 for *EL8

## Works as is
The Fedora Core 29 source rpm will rebuild on AlmaLinux8 as is.
ie

```` c
rpmbuild -rb SRPMS/tint2-16.6.1-1.fc29.src.rpm
````
should work fine once the prerequisites are met.

## Where tint2 is used
I use it with Openbox which is in the epel8 repository but tint2 and xlockmore are not.

## License
Basically GPL2+

## See Also
https://gitlab.com/o9000/tint2
