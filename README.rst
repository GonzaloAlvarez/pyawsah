=======
pyawsah
=======

**Retired.** Superseded by `awsutils <https://github.com/GonzaloAlvarez/awsutils>`_ —
see its ``awsdashboard``, a single-file rewrite of this tool's ``url`` command.

``awsdashboard`` does the same thing (pick a profile, pick a role, print a
federated console sign-in URL) with no package to install: one file, ``chmod
+x``, and a throwaway venv per run. It also fixes several bugs that were live
here — role listing was truncated at 100 and included service-linked roles,
role ARNs were synthesized rather than read, the session name was unvalidated,
and ``SessionDuration`` was sent with ``AssumeRole`` credentials, which the
federation endpoint rejects.

The ``newrole`` command was dropped rather than ported: it attached
``AdministratorAccess`` to a role trusting the account root, with no condition
and no confirmation.

This repository is archived and kept only for history.
