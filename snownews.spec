Summary:	Text mode RSS newsreader for Linux and Unix
Summary(pl.UTF-8):	Tekstowy czytnik newsów RSS dla Linuksa i innych Uniksów
Name:		snownews
Version:	1.5.12
Release:	1
License:	GPL v2
Group:		Applications/Networking
Source0:	http://kiza.kcore.de/software/snownews/download/%{name}-%{version}.tar.gz
# Source0-md5:	80da8943fc5aa96571924aec0087d4c0
URL:		http://kiza.kcore.de/software/snownews/
Patch0:		%{name}-FHS.patch
Patch1:		%{name}-home_etc.patch
Patch2:		%{name}-home_etc_utils.patch
Patch3:		%{name}-locales.patch
BuildRequires:	gettext-tools
BuildRequires:	libxml2-devel
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Snownews is a text mode RSS/RDF newsreader. It supports all versions
of RSS natively and supports other formats via plugins.

%description -l pl.UTF-8
Snownews jest tekstowym czytnikiem RSS/RDF. Posiada natywne wsparcie
dla wszystkich wersji RSS jak również, za pomocą wtyczek, dla innych
formatów.

%package utils
Summary:	Additional utilities for snownews
Summary(pl.UTF-8):	Dodatkowe narzędzia do snownews
Group:		Applications/Networking
Requires:	gnupg
Requires:	perl-XML-LibXML
Requires:	perl-XML-LibXSLT
Requires:	perl-libwww

%description utils
This package contains additional snownews utility: opml2snow.

%description utils -l pl.UTF-8
Ten pakiet zawiera dodatkowe narzędzie snownews: opml2snow.

%prep
%setup -q
%patch -P0 -p1
%patch -P1 -p1
%patch -P2 -p1
%patch -P3 -p1

mv po/uk_UA.po po/uk.po || exit 1
mv doc/man/ru_RU.KOI8-R doc/man/ru || exit 1
mv doc/man/ru/snownews.1.ru_RU.KOI8-R.in doc/man/ru/snownews.1.ru.in || exit 1

%build
./configure \
	--prefix=%{_prefix}

%{__make} \
	CC="%{__cc}" \
	EXTRA_CFLAGS="%{rpmcflags} -I/usr/include/ncursesw" \
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
%doc AUTHOR Changelog CREDITS README README.de README.patching
%attr(755,root,root) %{_bindir}/snownews
%{_mandir}/man1/snownews.1*
%lang(de) %{_mandir}/de/man1/snownews.1*
%lang(fr) %{_mandir}/fr/man1/snownews.1*
%lang(it) %{_mandir}/it/man1/snownews.1*
%lang(nl) %{_mandir}/nl/man1/snownews.1*
%lang(ru) %{_mandir}/ru/man1/snownews.1*

%files utils
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/opml2snow
%attr(755,root,root) %{_bindir}/snow2opml
%{_mandir}/man1/opml2snow.1*
