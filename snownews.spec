#
#TODO:
#	man files

Summary:	Text mode RSS newsreader for Linux and Unix.
Summary(pl):	Tekstowy czytnik newsów RSS dla Linuxa i innych Unixów
Name:		snownews
Version:	1.5.5.1
Release:	0.1
License:	GPL
Group:		Applications/Networking
Source0:	%{name}-%{version}.tar.gz
URL:		http://kiza.kcore.de/software/snownews/
Patch0:		%{name}-ncursesw.patch
Patch1:		%{name}-DESTDIR.patch
Patch2:		%{name}-manpath.patch
BuildRequires:	ncurses-devel
BuildRequires:	libxml2-devel
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snownews is a text mode RSS/RDF newsreader. It supports all versions
of RSS natively and supports other formats via plugins.

%prep
%setup -q -n %{name}-%{version}
%patch0	-p1
%patch1	-p1
%patch2	-p1

%build
./configure --prefix=/usr --charset=UTF-8
%{__make} all

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc CREDITS README
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
