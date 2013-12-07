# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/sides
# catalog-date 2007-02-26 21:24:31 +0100
# catalog-license gpl
# catalog-version undef
Name:		texlive-sides
Version:	20070226
Release:	5
Summary:	A LaTeX class for typesetting stage plays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sides
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sides.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sides.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is a LaTeX class for typesetting stage plays, based on the
plari class written by Antti-Juhani Kaijanaho in 1998. It has
been updated and several formatting changes have been made to
it--most noticibly there are no longer orphans.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/sides/sides.cls
%doc %{_texmfdistdir}/doc/latex/sides/README
%doc %{_texmfdistdir}/doc/latex/sides/sides-sample.pdf
%doc %{_texmfdistdir}/doc/latex/sides/sides-sample.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 20070226-2
+ Revision: 756024
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 20070226-1
+ Revision: 719534
- texlive-sides
- texlive-sides
- texlive-sides
- texlive-sides

