# dummy-docs

устанавливаем Sphinx, тему, расширение для краткого содержания в начале и расширение для копирования кода
`pip install sphinx sphinx-book-theme autodocsumm sphinx-copybutton`

инициализируем папку с документацией  
команда force_rewrite out_dir src_dir
`sphinx-apidoc -f -o docs/ src/`

создаём html-файлы
`sphinx-build docs/ docs/_build`
