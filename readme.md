WP Clean removes the Gutenberg style comments from the text version of a WordPress blog post. 

I wrote this because my blog uses Gutenberg, but the newspaper that republishes my posts uses a non-Gutenberg-enabled Wordpress. I got tired of editing these things out by hand. 

This script uses pyperclip, a Python module that makes it easy to use the clipboard. You can get pyperclip at https://pypi.org/project/pyperclip/ 

To use this: Copy the text version of your post to the clipboard by selecting it (Ctrl-A on Windows) and then copying it (Ctrl-C on Windows). Run the script. The text will be cleaned of Gutenberg-related comments and will pasted back to the clipboard. 

MIT License. Enjoy.