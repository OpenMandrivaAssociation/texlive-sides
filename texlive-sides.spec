%global tl_name sides
%global tl_revision 76924

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	A LaTeX class for typesetting stage plays
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/sides
License:	gpl
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sides.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/sides.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is a LaTeX class for typesetting stage plays, based on the plari
class written by Antti-Juhani Kaijanaho in 1998. It has been updated and
several formatting changes have been made to it--most noticeably there
are no longer orphans.

