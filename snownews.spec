#
# Conditional build:
%bcond_with	utf	# build with UTF-8 charset instead of ISO-8859-2
#
Summary:	Text mode RSS newsreader for Linux and Unix
Summary(pl):	Tekstowy czytnik newsów RSS dla Linuksa i innych Uniksów
Name:		snownews
Version:	1.5.6.1
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://kiza.kcore.de/software/snownews/download/%{name}-%{version}.tar.gz
# Source0-md5:	466ca82e8df03d6126d6cc0f20772025
URL:		http://kiza.kcore.de/software/snownews/
Patch0:		%{name}-FHS.patch
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

%package utils
Summary:	Additional utilities for snownews
Summary(pl):	Dodatkowe narzêdzia do snownews
Group:		Applications/Networking
Requires:	gnupg
Requires:	perl-libwww
Requires:	perl-XML-LibXML
Requires:	perl-XML-LibXSLT

%description utils
This package contains additional snownews utilities: opml2snow and
snowsync.

%description utils -l pl
Ten pakiet zawiera dodatkowe narzêdzia snownews: opml2snow i snowsync.

%prep
%setup -q
%patch0 -p1

%build
./configure \
	--prefix=%{_prefix} \
	--charset=%{?with_utf:UTF-8}%{!?with_utf:ISO-8859-2}

%{__make} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} -I%{_includedir}/ncurses%{?with_utf:w}" \
	EXTRA_LDFLAGS="%{rpmldflags}"

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
%attr(755,root,root) %{_bindir}/snownews
%{_mandir}/man1/snownews.1*
%lang(de) %{_mandir}/de/man1/snownews.1*
%lang(fr) %{_mandir}/fr/man1/snownews.1*
%lang(it) %{_mandir}/it/man1/snownews.1*
%lang(nl) %{_mandir}/nl/man1/snownews.1*
# XXX: no such dir, standard ru pages are in iso-8859-5 - convert?
%lang(ru) %{_mandir}/ru_RU.KOI8-R/man1/snownews.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/opml2snow
%attr(755,root,root) %{_bindir}/snowsync
%{_mandir}/man1/opml2snow.1*
