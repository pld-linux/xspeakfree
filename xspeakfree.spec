Summary:	Tcl/Tk frontend to speakfreely
Summary(pl):	Frontend do speakfreely napisany w tcl/tk
Name:		xspeakfree
Version:	0.8.1
Release:	1
Group:		Applications/Communication
Group(pl):	-
License:	public domain
Source0:	http://www.spearce.org/projects/xspeakfree/%{name}-%{version}.tar.gz
Patch0:		%{name}-executing.patch
URL:		http://www.spearce.org/projects/xspeakfree
Requires:	tk >= 8.0
Requires:	speakfreely
Requires:	/usr/bin/mkfifo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix	/usr/X11R6

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

install -d $RPM_BUILD_ROOT/{%{_bindir},%{_libdir}/%{name}}

install bin/* $RPM_BUILD_ROOT/%{_bindir}
install lib/%{name}/* $RPM_BUILD_ROOT/%{_libdir}/%{name}

gzip -9nf README HISTORY TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/*
%{_libdir}/%{name}/*

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: xspeakfree.spec,v $
Revision 1.1  2000-11-16 14:43:24  zagrodzki
- initial release
