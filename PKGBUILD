pkgname=lunar
pkgver=1.0
pkgrel=1
pkgdesc=""
arch=('x86_64')
url="https://github.com/Moon0day/lunar"
depends=()
makedepends=('gcc' 'make')
source=("git+https://github.com/Moon0day/lunar.git")
md5sums=('SKIP')

build() {
  cd "$srcdir/lunar"
  mkdir -p "$srcdir/lunar"
  cpp_files=$(find . -type f -name '*.cpp')
  g++ -std=c++17 $cpp_files -o luna
}

package() {
  cd "$srcdir/lunar"
  install -Dm755 luna "$pkgdir/usr/bin/luna"
}
