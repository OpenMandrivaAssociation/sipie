%define oname	Sipie

Summary:	Sirius streaming radio player
Name:		sipie
Version:	0.1196144357
Release:	%mkrel 3
Source0:	http://downloads.sourceforge.net/%{name}/%{oname}-%{version}.tar.gz
License:	GPLv2
Group:		Sound
URL:		http://sipie.sourceforge.net/
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	python
BuildRequires:	python-setuptools
BuildRequires:	python-devel
# Didn't work with the 3.0.3 package, this should help backports
# -AdamW 2008/06
Requires:	python-beautifulsoup >= 3.0.6-1mdv
Requires:	mplayer

%description
sipie is a player for Sirius online Internet streaming. It requires a
login to Sirius's streaming, and both guest and subscriber logins are 
supported. This package provides the back end and CLI front end. The
GTK+ front end is in the package sirius-gtk and the wxGTK front end
is in the package sirius-wx. The CLI front end can be run with the
command 'cliSipie'.

%package gtk
Summary:	Sirius streaming radio player GTK+ front end
Group:		Sound
Requires:	pygtk2
Requires:	%{name}

%description gtk
sipie is a player for Sirius online Internet streaming. It requires a
login to Sirius's streaming, and both guest and subscriber logins are 
supported. This package provides the GTK+ front end. You must run it
from a console (command gtkSipie), it cannot be run from the system
menus.

%package wx
Summary:	Sirius streaming radio player wxGTK front end
Group:		Sound
Requires:	wxPythonGTK
Requires:	%{name}

%description wx
sipie is a player for Sirius online Internet streaming. It requires a
login to Sirius's streaming, and both guest and subscriber logins are 
supported. This package provides the wxGTK front end. You must run it
from a console (command wxSipie), it cannot be run from the system
menus.

%prep
%setup -q -n %{oname}-%{version}

%install
rm -rf %{buildroot}
python setup.py install --root=%{buildroot} --compile --optimize=2

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%{_bindir}/cliSipie
%{_bindir}/sipie.py
%{py_puresitedir}/%{oname}-%{version}-py%{pyver}.egg-info
%{py_puresitedir}/%{oname}

%files gtk
%defattr(-,root,root)
%{_bindir}/gtkSipie

%files wx
%defattr(-,root,root)
%{_bindir}/wxSipie
