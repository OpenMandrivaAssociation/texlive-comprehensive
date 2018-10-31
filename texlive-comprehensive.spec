Name:		texlive-comprehensive
Version:	12.3
Release:	2
Summary:	Symbols accessible from LaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/info/symbols/comprehensive
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comprehensive.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/comprehensive.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg

%description
Around 5000 symbols are listed as a set of tables. The tables
of symbols are ordered in a logical way (the document begins
with a 'frequently requested symbols' list), the aim being to
make the document a convenient way of looking up symbols.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/latex/comprehensive

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
