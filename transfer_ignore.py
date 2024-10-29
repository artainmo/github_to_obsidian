import re

dir_pattern = r"""
    ^.*\.xcworkspace$|
    ^.*\.xcodeproj$|
    ^.*/utils/ft_printf$|
    ^.*/utils/get_next_line$|
    ^.*/utils/libft$|
    ^.*/libs/get_next_line$|
    ^.*/libs/libft$|
    ^.*/utils/minilibX$|
    ^inception-of-things/p1$|
    ^inception-of-things/p2$|
    ^matcha/frontend$|
    ^minishell-unittest/test/test$|
    ^.*/data$|
    ^.*/node_modules$|
    ^.*/js/vendor$|
    ^webserv/conf$|
    ^webserv/webserv/frontend$|
    ^ft_printf/ft_printf$
"""
# 're.compile' compiles a regular expression pattern into a regex object
# 're.VERBOSE' allows comments and line breaks within the regex, making it more maintainable.
dir_compiled_pattern = re.compile(dir_pattern, re.VERBOSE)

file_pattern = r"""
    ^.*\.gitkeep$|
    ^.*\.swp$|
    ^a\.out$|
    ^.*/a\.out$|
    ^.*\.env$|
    ^.*\.txt$|
    ^.*\.zip$|
    ^.*\.csv$|
    ^.*\.svg$|
    ^.*\.png$|
    ^.*\.jpg$|
    ^.*\.ico$|
    ^.*\.json$|
    ^.*\.storyboard$|
    ^.*\.plist$|
    ^telegraf\.conf$|
    ^.*/telegraf\.conf$|
    ^grafana\.db$|
    ^.*/grafana\.db$|
    ^wordpress\.sql$|
    ^.*/wordpress\.sql$|
    ^.*\.eslintrc\.js$|
    ^.*\.prettierrc$|
    ^.*\.lock$|
    ^.*\.options$|
    ^.*\.conf\.in$|
    ^.*\.map$|
    ^.*\.pdf$|
    ^.*\.bmp$|
    ^.*\.rt$|
    ^.*\.names$|
    ^.*\.pkl$|
    ^.*\.log$|
    ^reportWebVitals\.js$|
    ^.*/reportWebVitals\.js$|
    ^.*app\.e2e-spec\.ts$
"""
file_compiled_pattern = re.compile(file_pattern, re.VERBOSE)

def filter_dirs(path):
    return bool(dir_compiled_pattern.match(path))

def files_with_no_extension(path):
    return not path.lower().endswith(("makefile", "dockerfile"))

def filter_files(path):
    if '.' in path:
        return bool(file_compiled_pattern.match(path))
    else:
        return files_with_no_extension(path)
