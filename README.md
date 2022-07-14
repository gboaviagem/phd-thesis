# phd-thesis
TeX files for my PhD Thesis.

### Adding to the local repository an Overleaf Git remote
As explained by [Overleaf](https://www.overleaf.com/learn/how-to/Using_Git_and_GitHub),
one can link this Github repository with the (paid) Overleaf project, after cloning locally,
by doing so:
```sh
$ cd phd-thesis
$ git remote add overleaf https://git.overleaf.com/62d0772f6d2da3875ac89c64
```

Now,
```sh
$ git remote -v
origin	https://github.com/gboaviagem/phd-thesis.git (fetch)
origin	https://github.com/gboaviagem/phd-thesis.git (push)
overleaf	https://git.overleaf.com/62d0772f6d2da3875ac89c64 (fetch)
overleaf	https://git.overleaf.com/62d0772f6d2da3875ac89c64 (push)
```

To pull the latest content from the Overleaf project and merge it into your `main` branch,
```sh
$ git pull overleaf master --allow-unrelated-histories
```

Since the main branch in Overlear if `master`, the push will go a bit differently, in the first time:
```sh
$ git push -u overleaf main:master
```
