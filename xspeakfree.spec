Summary:	Tcl/Tk frontend to speakfreely
Summary(pl):	Frontend do speakfreely napisany w Tcl/Tk
Name:		xspeakfree
Version:	0.8.1
Release:	1
Group:		Applications/Communications
License:	Public Domain
Source0:	http://www.spearce.org/projects/xspeakfree/%{name}-%{version}.tar.gz
# Source0-md5:	6589d49433ab5993945f49329e3a27bd
Patch0:		%{name}-executing.patch
URL:		http://www.spearce.org/projects/xspeakfree/
Requires:	/usr/bin/mkfifo
Requires:	speakfreely
Requires:	tk >= 8.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
xspeakfree is a Tcl/Tk (wish) frontend to Speak Freely.

%description -l pl
xspeakfree jest frontendem w Tcl/Tk (wish) do Speak Freely.

%prep
%setup  -q
%patch0 -p1

%build

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT{%{_bindir},%{_libdir}/%{name}}

install bin/* $RPM_BUILD_ROOT%{_bindir}
install lib/%{name}/* $RPM_BUILD_ROOT%{_libdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README HISTORY TODO
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}/*
