# RPM spec for envconsul

* Binary: `/usr/bin/envconsul`

# How to build

* Check out this repo.
* Ensure that `rpmdevtools` and `mock` are available:
```
$ sudo yum install rpmdevtools mock
```
* Get with the build tree.
```
$ rpmdev-setuptree
```
* Copy spec.
```
$ cp envconsul-rpm/SPECS/envconsul.spec rpmbuild/SPECS/
```
* Download the release tarball.
```
$ spectool -g -R rpmbuild/SPECS/envconsul.spec
```
* And build.
```
$ rpmbuild -ba rpmbuild/SPECS/envconsul.spec
```
## Releases envconsul

https://releases.hashicorp.com/envconsul/

## Sources envconsul

https://github.com/hashicorp/envconsul
