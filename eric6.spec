%bcond_with	python2 # Use python2 (NOTE: as for 17.03.1 it has issuses in PLD)

# NOTE: Detlev Offenbach <detlev@die-offenbachs.de> (author) 2017/04/13 wrote:
# "eric6 can be used with  Python2 or Python3 and with PyQt5 or PyQt4. 
# However, the recommended combination is PyQt5 on Python3.

%define		module	eric6
Summary:	Eric6 - a full featured Python IDE
Summary(pl.UTF-8):	Eric6 - pełnowartościowe IDE dla Pythona
Name:		eric6
Version:	17.07
Release:	8
License:	GPL v3
Group:		Libraries/Python
Source0:	https://sourceforge.net/projects/eric-ide/files/eric6/stable/%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c21c097bf36259ff61187e2698b7c50d
Patch0:		python3.patch
URL:		http://eric-ide.python-projects.org/index.html
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
%if %{with python2}
BuildRequires:	python-modules
BuildRequires:	python-setuptools
# NOTE: As for 6.1.8  eric6 still tries to import PyQt5 while having PyQt4 leading to crash
#	http://die-offenbachs.homelinux.org:48888/issues/issue204
# for --pyqt=4
# BuildRequires:	python-PyQt4-qscintilla2
# BuildRequires:	python-PyQt4-uic
# for --pyqt=5
BuildRequires:	python-PyQt5-qscintilla2
BuildRequires:	python-PyQt5-uic
Requires:	python-PyQt5-qscintilla2
Requires:	python-modules
Suggests:	python-pylint
%else
BuildRequires:	python3-PyQt5-qscintilla2
BuildRequires:	python3-PyQt5-uic
BuildRequires:	python3-modules
BuildRequires:	python3-setuptools
# NOTE: Not sure if Qt5Svg should be listed here or be R by other BRs.
BuildRequires:	Qt5Svg
Requires:	python3-PyQt5-qscintilla2
Requires:	python3-modules
Suggests:	python3-pylint
%endif

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
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT
%if %{with python2}
python install.py -z -c -b %{_bindir} -d %{py_sitescriptdir} -i $RPM_BUILD_ROOT  --pyqt=5
%else
python3 install.py -z -c -b %{_bindir} -d %{py3_sitescriptdir} -i $RPM_BUILD_ROOT  --pyqt=5
%endif
mkdir $RPM_BUILD_ROOT%{_datadir}/appdata
mv $RPM_BUILD_ROOT%{_datadir}/metainfo/eric6.appdata.xml $RPM_BUILD_ROOT%{_datadir}/appdata

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.rst
%if %{with python2}
%{py_sitescriptdir}/%{module}
%else
%{py3_sitescriptdir}/%{module}
%endif

%attr(755,root,root) %{_bindir}/eric6
%attr(755,root,root) %{_bindir}/eric6_*
# for --pyqt=4
# %{_datadir}/qt4/qsci/api/qss/
# %{_datadir}/qt4/qsci/api/ruby/
# NOTE: file %{_datadir}/qt4/qsci/api/ruby/Ruby-1.8.7.api from install of eric6-6.1.8-0.1.noarch conflicts with file from package eric4-4.5.24-3.noarch
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
%{_desktopdir}/eric6_browser.desktop
%{_datadir}/appdata/eric6.appdata.xml
%if %{with python2}
%{py_sitescriptdir}/eric6config.py
%{py_sitescriptdir}/eric6plugins
%else
%{py3_sitescriptdir}/eric6config.py
%{py3_sitescriptdir}/eric6plugins
%endif
