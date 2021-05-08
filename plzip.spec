Summary:	Parallel LZMA file compressor
Summary(pl.UTF-8):	Równoległy kompresor plików oparty na algorytmie LZMA
Name:		plzip
Version:	1.9
Release:	1
License:	GPL v3+
Group:		Applications/Archiving
Source0:	http://download.savannah.gnu.org/releases/lzip/plzip/%{name}-%{version}.tar.lz
# Source0-md5:	b36be328f73c8b9c0338d39d620265e9
Patch0:		%{name}-info.patch
URL:		http://savannah.nongnu.org/projects/lzip/
BuildRequires:	libstdc++-devel
BuildRequires:	lzip
BuildRequires:	lzlib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	texinfo
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Plzip is a massively parallel (multi-threaded), lossless data
compressor based on the lzlib compression library, with a user
interface similar to the one of lzip, bzip2 or gzip.

Plzip can compress/decompress large files on multiprocessor machines
much faster than lzip, at the cost of a slightly reduced compression
ratio. On files large enough (several GB), plzip can use hundreds of
processors. On files of only a few MB it is better to use lzip.

%description -l pl.UTF-8
Plzip to intensywnie zrównoleglony (wielowątkowy) bezstratny kompresor
danych oparty na bibliotece lzlib, z interfejsem użytkownika podobnym
do programów lzip, bzip2 i gzip.

Plzip potrafi kompresować/dekompresować duże pliki na maszynach
wieloprocesorowych szybciej niż lzip kosztem nieco mniejszego
współczynnika kompresji. Dla plików wystarczająco dużych (kilka GB)
plzip potrafi użyć setek procesorów. Dla plików mających tylko kilka
MB lepiej używać lzipa.

%prep
%setup -q
%patch0 -p1

%build
%configure
%{__make} all info

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%postun	-p /sbin/postshell
-/usr/sbin/fix-info-dir -c %{_infodir}

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_bindir}/plzip
%{_mandir}/man1/plzip.1*
%{_infodir}/plzip.info*
