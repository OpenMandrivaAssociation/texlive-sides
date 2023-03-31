Name:		texlive-sides
Version:	15878
Release:	2
Summary:	A LaTeX class for typesetting stage plays
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/sides
License:	GPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sides.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/sides.doc.r%{version}.tar.xz
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
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
