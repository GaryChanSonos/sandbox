set nocompatible " be iMproved, required
filetype off " required

" set the runtime path to include Vundle and initialize
set rtp+=~/.vim/bundle/Vundle.vim
call vundle#begin()
" alternatively, pass a path where Vundle should install plugins
"call vundle#begin('~/some/path/here')

" let Vundle manage Vundle, required
Plugin 'VundleVim/Vundle.vim'
Plugin 'tpope/vim-sensible'
Plugin 'lifepillar/vim-solarized8'

set termguicolors
let &t_8f = "\<Esc>[38;2;%lu;%lu;%lum"
let &t_8b = "\<Esc>[48;2;%lu;%lu;%lum"

set background=dark
colorscheme solarized8
syntax enable
"set number relativenumber
set wildmenu
set showcmd
set incsearch
set hlsearch
set ignorecase
set smartcase
set ruler
set laststatus=2
set cmdheight=2
set shiftwidth=4
set tabstop=4
set softtabstop=4
set expandtab
set cursorline
set showmatch
"set mouse=r 
set clipboard=unnamed

" All of your Plugins must be added before the following line 
call vundle#end() " required 
filetype plugin indent on " required

