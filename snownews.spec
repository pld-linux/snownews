# TODO:
# - something wrong with charset
#
# Conditional build:
%bcond_with	iso2	# build with ISO-8859-2 charset instead of UTF-8
#
Summary:	Text mode RSS newsreader for Linux and Unix
Summary(pl):	Tekstowy czytnik newsów RSS dla Linuksa i innych Uniksów
Name:		snownews
Version:	1.5.6.1
Release:	0.2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://kiza.kcore.de/software/snownews/download/%{name}-%{version}.tar.gz
# Source0-md5:	466ca82e8df03d6126d6cc0f20772025
URL:		http://kiza.kcore.de/software/snownews/
Patch0:		%{name}-ncursesw.patch
Patch1:		%{name}-FHS.patch
BuildRequires:	gettext-devel
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snownews is a text mode RSS/RDF newsreader. It supports all versions
of RSS natively and supports other formats via plugins.

%description -l pl
Snownews jest tekstowym czytnikiem RSS/RDF. Posiada natywne wsparcie
dla wszystkich wersji RSS jak równie¿, za pomoc± wtyczek, dla innych
formatów.

%prep
%setup -q
%patch0	-p1
%patch1 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--charset=%{?with_iso2:ISO-8859-2}%{!?with_iso2:UTF-8}

%{__make} \
	CC="%{__cc}"
	CFLAGS="%{rpmcflags}" \
	LDFLAGS="%{rpmldflags}"

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
%doc CREDITS README README.colors
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man[15]/*
%lang(de) %{_mandir}/de/man1/*
%lang(fr) %{_mandir}/fr/man1/*
%lang(it) %{_mandir}/it/man1/*
%lang(nl) %{_mandir}/nl/man1*/
# XXX: no such dir, standard ru pages are in iso-8859-5 - convert?
%lang(ru) %{_mandir}/ru_RU.KOI8-R/man1/*
