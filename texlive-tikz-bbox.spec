%global tl_name tikz-bbox
%global tl_revision 57444

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.1
Release:	%{tl_revision}.1
Summary:	Precise determination of bounding boxes in TikZ
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/graphics/pgf/contrib/tikz-bbox
License:	lppl1.3c
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bbox.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/tikz-bbox.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The built-in determination of the bounding box in TikZ is not entirely
accurate. This is because, for Bezier curves, it is the smallest box
that contains all control points, which is in general larger than the
box that just contains the curve. This library determines the exact
bounding box of the curve.

