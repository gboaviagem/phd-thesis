pstricks2eps(){
latex "$1".tex; dvips "$1".dvi -E -o "$1".eps
}
