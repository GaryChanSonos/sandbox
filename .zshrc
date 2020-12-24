# Enable Powerlevel10k instant prompt. Should stay close to the top of ~/.zshrc.
# Initialization code that may require console input (password prompts, [y/n]
# confirmations, etc.) must go above this block; everything else may go below.
if [[ -r "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh" ]]; then
  source "${XDG_CACHE_HOME:-$HOME/.cache}/p10k-instant-prompt-${(%):-%n}.zsh"
fi

# If you come from bash you might have to change your $PATH.
# export PATH=$HOME/bin:/usr/local/bin:$PATH

# Path to your oh-my-zsh installation.
export ZSH="/Users/gary.chan/.oh-my-zsh"

# Set name of the theme to load --- if set to "random", it will
# load a random theme each time oh-my-zsh is loaded, in which case,
# to know which specific one was loaded, run: echo $RANDOM_THEME
# See https://github.com/ohmyzsh/ohmyzsh/wiki/Themes
#ZSH_THEME="my_awesome_theme"
ZSH_THEME="powerlevel10k/powerlevel10k"

# Set list of themes to pick from when loading at random
# Setting this variable when ZSH_THEME=random will cause zsh to load
# a theme from this variable instead of looking in ~/.oh-my-zsh/themes/
# If set to an empty array, this variable will have no effect.
# ZSH_THEME_RANDOM_CANDIDATES=( "robbyrussell" "agnoster" )

# Uncomment the following line to use case-sensitive completion.
# CASE_SENSITIVE="true"

# Uncomment the following line to use hyphen-insensitive completion.
# Case-sensitive completion must be off. _ and - will be interchangeable.
# HYPHEN_INSENSITIVE="true"

# Uncomment the following line to disable bi-weekly auto-update checks.
# DISABLE_AUTO_UPDATE="true"

# Uncomment the following line to automatically update without prompting.
# DISABLE_UPDATE_PROMPT="true"

# Uncomment the following line to change how often to auto-update (in days).
# export UPDATE_ZSH_DAYS=13

# Uncomment the following line if pasting URLs and other text is messed up.
# DISABLE_MAGIC_FUNCTIONS=true

# Uncomment the following line to disable colors in ls.
# DISABLE_LS_COLORS="true"

# Uncomment the following line to disable auto-setting terminal title.
# DISABLE_AUTO_TITLE="true"

# Uncomment the following line to enable command auto-correction.
# ENABLE_CORRECTION="true"

# Uncomment the following line to display red dots whilst waiting for completion.
# COMPLETION_WAITING_DOTS="true"

# Uncomment the following line if you want to disable marking untracked files
# under VCS as dirty. This makes repository status check for large repositories
# much, much faster.
# DISABLE_UNTRACKED_FILES_DIRTY="true"

# Uncomment the following line if you want to change the command execution time
# stamp shown in the history command output.
# You can set one of the optional three formats:
# "mm/dd/yyyy"|"dd.mm.yyyy"|"yyyy-mm-dd"
# or set a custom format using the strftime function format specifications,
# see 'man strftime' for details.
# HIST_STAMPS="mm/dd/yyyy"

# Would you like to use another custom folder than $ZSH/custom?
# ZSH_CUSTOM=/path/to/new-custom-folder

# Which plugins would you like to load?
# Standard plugins can be found in ~/.oh-my-zsh/plugins/*
# Custom plugins may be added to ~/.oh-my-zsh/custom/plugins/
# Example format: plugins=(rails git textmate ruby lighthouse)
# Add wisely, as too many plugins slow down shell startup.
plugins=(git zsh-autosuggestions git-extras docker vagrant)

source $ZSH/oh-my-zsh.sh

# User configuration

# export MANPATH="/usr/local/man:$MANPATH"

# You may need to manually set your language environment
# export LANG=en_US.UTF-8

# Preferred editor for local and remote sessions
# if [[ -n $SSH_CONNECTION ]]; then
#   export EDITOR='vim'
# else
#   export EDITOR='mvim'
# fi

# Compilation flags
# export ARCHFLAGS="-arch x86_64"

# Set personal aliases, overriding those provided by oh-my-zsh libs,
# plugins, and themes. Aliases can be placed here, though oh-my-zsh
# users are encouraged to define aliases within the ZSH_CUSTOM folder.
# For a full list of active aliases, run `alias`.
#
# Example aliases
alias zshrc="vim ~/.zshrc"
# alias ohmyzsh="mate ~/.oh-my-zsh"

# Credentials
source "$HOME/.credentials"

# Perforce
export P4PORT=ssl:p4p-bos.sonos.com:1666
export P4EDITOR=vim
export P4DIFF=vimdiff
export P4MERGE=p4merge
export P4CONFIG=.p4config
export P4IGNORE=.p4ignore

# Automation
export EXECUTION_ENVIRONMENT="$HOME/testbed.json"
export JAVA_HOME=`/usr/libexec/java_home -v 1.8`
export GROOVY_HOME=/Users/gary.chan/.sdkman/candidates/groovy/current/bin/groovy
export PATH=$PATH:~/.android-sdk-macosx/platform-tools/
export VAGRANT_DEFAULT_PROVIDER=virtualbox
export PYTHONSTARTUP="$HOME/.pythonrc.py"
export SPOTIFY_KEY="garychansonos/US/AQCgVxgmDNTVdZxT8mQAUSRO2y0Mqs-qN9JGh3Gl3C8Ve-chqmlzfb6CLu0imbDNEBlB0y0wh3OcE1IL9-5sqY6wBGRGo1H_jb39CmLZaD1VZcnPdw3BVVnMzYgRwtYYgHY/1593743366806"
export SPOTIFY_TOKEN="BQB_Bm_abL7_DCXUOcPxnoAXQVITdrAzq7FtB24vq7R9K53TGfc7rINYAMl5AIf-A4xTxJf-CihAYHu1eiJTJ7O-wy1bR00CoGtx8mmyLFjZ1mT6M08Qb0Fil0aW9JwrA5ZBrgdGuWxfd3re1tvCWg9tokeU1S0N_2EE4iWVFOVb5EmReQ4rd9hSGCfuf5rg1q2JvQOpuXs28Owv1GkUKtFtTVI59Szt45IfiDyfDuaF5wXI0mXxjFhGaV4zMxmArPpo"

# Dynamo DB
export DYNAMO_ENDPOINT="http://localhost:8000"

#THIS MUST BE AT THE END OF THE FILE FOR SDKMAN TO WORK!!!
export SDKMAN_DIR="/Users/gary.chan/.sdkman"
[[ -s "/Users/gary.chan/.sdkman/bin/sdkman-init.sh" ]] && source "/Users/gary.chan/.sdkman/bin/sdkman-init.sh"

export PATH="/usr/local/opt/gettext/bin:$PATH"

# iTerm2
test -e "${HOME}/.iterm2_shell_integration.zsh" && source "${HOME}/.iterm2_shell_integration.zsh"

#export PATH="/usr/local/sbin:$PATH"

# rbenv
#export RUBY_CONFIGURE_OPTS="--with-openssl-dir=$(brew --prefix openssl@1.1)"
eval "$(rbenv init -)"
#eval "$(rbenv init --no-rehash -)"
#(rbenv rehash &) 2> /dev/null

# nvm
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"  # This loads nvm
[ -s "$NVM_DIR/bash_completion" ] && \. "$NVM_DIR/bash_completion"  # This loads nvm bash_completion

# tabtab source for packages
# uninstall by removing these lines
[[ -f ~/.config/tabtab/__tabtab.zsh ]] && . ~/.config/tabtab/__tabtab.zsh || true
if command -v pyenv 1>/dev/null 2>&1; then
  eval "$(pyenv init -)"
fi

# To customize prompt, run `p10k configure` or edit ~/.p10k.zsh.
[[ ! -f ~/.p10k.zsh ]] || source ~/.p10k.zsh

# tabtab source for serverless package
# uninstall by removing these lines or running `tabtab uninstall serverless`
[[ -f /Users/gary.chan/git/pdsw-services-content-catalog-poc-2018/node_modules/tabtab/.completions/serverless.zsh ]] && . /Users/gary.chan/git/pdsw-services-content-catalog-poc-2018/node_modules/tabtab/.completions/serverless.zsh
# tabtab source for sls package
# uninstall by removing these lines or running `tabtab uninstall sls`
[[ -f /Users/gary.chan/git/pdsw-services-content-catalog-poc-2018/node_modules/tabtab/.completions/sls.zsh ]] && . /Users/gary.chan/git/pdsw-services-content-catalog-poc-2018/node_modules/tabtab/.completions/sls.zsh

# direnv
eval "$(direnv hook zsh)"

# Load in automation settings...
if [ -f ~/.automationrc ]; then
    . ~/.automationrc
fi
