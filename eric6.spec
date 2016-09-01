# TODO: Switch to python3

%define 	module	eric6
Summary:	Eric6 - a full featured Python IDE
Summary(pl.UTF-8):	Eric6 - pełnowartościowe IDE dla Pythona
# Name must match the python module/package name (as on pypi or in 'import' statement)
Name:		eric6
Version:	6.1.8
Release:	0.5
License:	GPL v3
Group:		Libraries/Python
Source0:	https://sourceforge.net/projects/eric-ide/files/eric6/stable/%{version}/eric6-%{version}.tar.gz
# Source0-md5:	a070c679fbc93fab4f3b718a5875e5d0
URL:		http://eric-ide.python-projects.org/index.html
BuildRequires:	rpm-pythonprov
# for the py_build, py_install macros
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
# NOTE: As for 6.1.8  eric6 still tries to import PyQt5 while having PyQt4 leading to crash
# 	http://die-offenbachs.homelinux.org:48888/issues/issue204
# for --pyqt=4
# BuildRequires:	python-PyQt4-qscintilla2
# BuildRequires:	python-PyQt4-uic
# for --pyqt=5
BuildRequires:	python-PyQt5-qscintilla2
BuildRequires:	python-PyQt5-uic

%endif
%if %{with python3}
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
%endif
Requires:	python-modules
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Eric is a Python IDE written using PyQt and QScintilla. It provides
various features such as any number of open editors, an integrated
(remote) debugger, project management facilities, unit test,
refactoring and much more.

%description -l pl.UTF-8
Eric jest pythonowym graficznym środowiskiem programistycznym
używającym PyQt i QScintilla.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT
python install.py -z -c -b %{_bindir} -d %{py_sitescriptdir} -i $RPM_BUILD_ROOT  --pyqt=5

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.rst
%{py_sitescriptdir}/%{module}
%attr(755,root,root) %{_bindir}/eric6
%attr(755,root,root) %{_bindir}/eric6_*
# for --pyqt=4
# %{_datadir}/qt4/qsci/api/qss/
# %{_datadir}/qt4/qsci/api/ruby/
# %{_datadir}/qt4/qsci/api/python/eric6.*
# %{_datadir}/qt4/qsci/api/python/zope-*.api

# for --pyqt=5
%{_datadir}/qt5/qsci/api/qss/
%{_datadir}/qt5/qsci/api/ruby/
%{_datadir}/qt5/qsci/api/python/eric6.*
%{_datadir}/qt5/qsci/api/python/zope-*.api

%{_pixmapsdir}/eric*.png
%{_desktopdir}/eric6.desktop
%{_desktopdir}/eric6_webbrowser.desktop
%{_datadir}/appdata/eric6.appdata.xml
# file %{_datadir}/qt4/qsci/api/ruby/Ruby-1.8.7.api from install of eric6-6.1.8-0.1.noarch conflicts with file from package eric4-4.5.24-3.noarch
%{py_sitescriptdir}/eric6config.py
%{py_sitescriptdir}/eric6plugins
%endif
