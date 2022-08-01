%define lua_dir	%{_datarootdir}/lua
%define lua_dir_resty	%{lua_dir}/5.3/resty

Name: lua-resty-string
Summary: String utilities and common hash functions for ngx_lua and LuaJIT
Version: 0.15
Release: 3
URL: https://github.com/yoannguion/lua-resty-string
License: BSD
Provides: String utilities and common hash functions for ngx_lua and LuaJIT
Requires: lua-resty-string
BuildArch: noarch

%description
String utilities and common hash functions for ngx_lua and LuaJIT



%install
mkdir -p $RPM_BUILD_ROOT%{lua_dir_resty}
cp -rf %{_sourcedir}/lib/resty/* $RPM_BUILD_ROOT%{lua_dir_resty}

%files
%{lua_dir_resty}/aes.lua
%{lua_dir_resty}/md5.lua
%{lua_dir_resty}/random.lua
%{lua_dir_resty}/sha.lua
%{lua_dir_resty}/sha1.lua
%{lua_dir_resty}/sha224.lua
%{lua_dir_resty}/sha256.lua
%{lua_dir_resty}/sha384.lua
%{lua_dir_resty}/sha512.lua
%{lua_dir_resty}/string.lua



%changelog
* Mon Aug 01 2022 Yoann GUION <yoann.guion@gmail.com> - 0.15-3
- Initial release 0.15
