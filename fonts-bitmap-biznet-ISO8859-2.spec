Summary:	biznet ISO-8859-2 bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe biznet ISO-8859-2
Name:		fonts-bitmap-biznet-ISO8859-2
Version:	0
Release:	1
License:	MIT
Group:		Fonts
# originally from http://www.biz.net.pl/images/ (404 now)
Source0:	ISO8859-2-bdf.tar.gz
# Source0-md5:	5dd69ab949d833944048b10a97f7a589
BuildRequires:	xorg-app-bdftopcf
Requires(post,postun):	fontpostinst
Requires:	%{_fontsdir}/misc
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The BIZNET ISO 8859-2 (Central European) X Window System Fonts have
been derived from the original ISO 8859-1 fonts included in the X
Window System, Version 11, Release 6.3 distribution (X11R6.3).

This package contains only selected fonts which counterparts in
base X11 distribution don't include ISO-8859-2 characters.

%description -l pl.UTF-8
Fonty BIZNET ISO 8859-2 (środkowoeuropejskie) dla X Window System
wywodzą się z oryginalnych fontów ISO 8859-1 z dystrybucji X Window
System w wersji 11, wydaniu 6.3 (X11R6.3).

Ten pakiet zawiera tylko wybrane fonty, których odpowiedniki z
podstawowej dystrybucji X11 nie zawierają znaków ISO-8859-2.

%package 75dpi
Summary:	biznet ISO-8859-2 75dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe 75dpi biznet ISO-8859-2
Group:		Fonts

%description 75dpi
The BIZNET ISO 8859-2 (Central European) X Window System Fonts have
been derived from the original ISO 8859-1 fonts included in the X
Window System, Version 11, Release 6.3 distribution (X11R6.3).

This package contains only selected 75dpi fonts which counterparts in
base X11 distribution don't include ISO-8859-2 characters.

%description 75dpi -l pl.UTF-8
Fonty BIZNET ISO 8859-2 (środkowoeuropejskie) dla X Window System
wywodzą się z oryginalnych fontów ISO 8859-1 z dystrybucji X Window
System w wersji 11, wydaniu 6.3 (X11R6.3).

Ten pakiet zawiera tylko wybrane fonty 75dpi, których odpowiedniki z
podstawowej dystrybucji X11 nie zawierają znaków ISO-8859-2.

%package 100dpi
Summary:	biznet ISO-8859-2 100dpi bitmap fonts
Summary(pl.UTF-8):	Fonty bitmapowe 100dpi biznet ISO-8859-2
Group:		Fonts

%description 100dpi
The BIZNET ISO 8859-2 (Central European) X Window System Fonts have
been derived from the original ISO 8859-1 fonts included in the X
Window System, Version 11, Release 6.3 distribution (X11R6.3).

This package contains only selected 100dpi fonts which counterparts in
base X11 distribution don't include ISO-8859-2 characters.

%description 100dpi -l pl.UTF-8
Fonty BIZNET ISO 8859-2 (środkowoeuropejskie) dla X Window System
wywodzą się z oryginalnych fontów ISO 8859-1 z dystrybucji X Window
System w wersji 11, wydaniu 6.3 (X11R6.3).

Ten pakiet zawiera tylko wybrane fonty 100dpi, których odpowiedniki z
podstawowej dystrybucji X11 nie zawierają znaków ISO-8859-2.

%prep
%setup -q -c

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_fontsdir}/{75dpi,100dpi,misc}

# other fonts in xorg-font-* already include ISO-8859-2 chars
for f in misc/12x24.bdf misc/8x16.bdf ; do
	bdftopcf $f | gzip -9n > $RPM_BUILD_ROOT%{_fontsdir}/misc/`basename $f .bdf`-ISO8859-2.pcf.gz
done
for f in 75dpi/char*.bdf 75dpi/term*.bdf ; do
	bdftopcf $f | gzip -9n > $RPM_BUILD_ROOT%{_fontsdir}/75dpi/`basename $f .bdf`-ISO8859-2.pcf.gz
done
for f in 100dpi/char*.bdf 100dpi/term*.bdf ; do
	bdftopcf $f | gzip -9n > $RPM_BUILD_ROOT%{_fontsdir}/100dpi/`basename $f .bdf`-ISO8859-2.pcf.gz
done

grep -e '-biznet-fixed-medium-r-normal--16-120-100-100-c-80-iso8859-2\|-biznet-fixed-medium-r-normal--24-170-100-100-c-120-iso8859-2' misc/fonts.alias > $RPM_BUILD_ROOT%{_fontsdir}/misc/fonts.alias.%{name}
grep -e 'biznet-\(chartis\|terminal\)' 75dpi/fonts.alias \
	> $RPM_BUILD_ROOT%{_fontsdir}/75dpi/fonts.alias.%{name}-75dpi
grep -e 'biznet-\(chartis\|terminal\)' 100dpi/fonts.alias \
	> $RPM_BUILD_ROOT%{_fontsdir}/100dpi/fonts.alias.%{name}-100dpi

%clean
rm -rf $RPM_BUILD_ROOT

%post
fontpostinst misc

%postun
fontpostinst misc

%post 75dpi
fontpostinst 75dpi

%postun 75dpi
fontpostinst 75dpi

%post 100dpi
fontpostinst 100dpi

%postun 100dpi
fontpostinst 100dpi

%files
%defattr(644,root,root,755)
%doc RELEASE_NOTES.TXT
%{_fontsdir}/misc/*.pcf.gz
%{_fontsdir}/misc/fonts.alias.%{name}

%files 75dpi
%defattr(644,root,root,755)
%doc RELEASE_NOTES.TXT
%{_fontsdir}/75dpi/*.pcf.gz
%{_fontsdir}/75dpi/fonts.alias.%{name}-75dpi

%files 100dpi
%defattr(644,root,root,755)
%doc RELEASE_NOTES.TXT
%{_fontsdir}/100dpi/*.pcf.gz
%{_fontsdir}/100dpi/fonts.alias.%{name}-100dpi
