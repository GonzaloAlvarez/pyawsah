========================
Python AWS Access Helper
========================


Python AWS Client to get Access through the console based on a profile, which provides AWS credentials


* Free software: MIT license
* Documentation: https://pyawsah.readthedocs.io.


Features
--------

* List aws profiles in your local machine
* Create a role that has administration priviledges
* Create an STS token
* Derive the URI to access the AWS console from a federated model in one click

Usage
-------

Show a list of profiles available on the machine:
.. code::shell
  $ pyawsah profiles

Show a list of roles that the aws account associated witht the profile has available
.. code::shell
  $ pyawsah roles --profile [profilename]

Create a new role with administrator priviledges and a specific name
.. code::shell
  $ pyawsah newrole --profile [profilename] --name [rolename]

Generate the URL of a federated console access
.. code::shell
  $ pyawsah url --profile [profilename] --role [rolename]
