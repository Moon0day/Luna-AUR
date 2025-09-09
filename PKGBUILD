pkgname=luna
pkgver=1.0
pkgrel=1
pkgdesc="Luna AUR package - builds all C++ source files"
arch=('x86_64')
url="https://github.com/Moon0day/Luna-AUR"
depends=()
makedepends=('gcc' 'make')
source=("git+https://github.com/Moon0day/Luna-AUR.git")
md5sums=('SKIP')

build() {
  cd "$srcdir/Luna-AUR"
  cpp_files=$(find . -type f -name '*.cpp')
  g++ -std=c++17 $cpp_files -o luna
}

package() {
  cd "$srcdir/Luna-AUR"
  install -Dm755 luna "$pkgdir/usr/bin/luna"
}
