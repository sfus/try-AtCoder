README
---

## Setup online-judge-tools and atcoder-cli

```
$ pip3 install online-judge-tools
$ npm install -g atcoder-cli
```

## How to prepare for `atcoder-cli` after install

```
$ acc login
$ oj login https://atcoder.jp/
$ acc config default-test-dirname-format test
```

(note: The default value of `default-test-dirname-format` is `tests`, but `oj test` command requires `test` directory)

## GNU time for `oj test`

If in MacOS, install GNU time and add alias to override MacOS's `/usr/bin/time` for `oj test`.
```
$ brew install gnu-time
$ ln -s /usr/local/bin/gtime /usr/local/bin/time
```

Otherwise, you'll face the following error.
```
time: illegal option -- f
usage: time [-lp] command.
[!] GNU time is not available: time
```

## How to solve and submit atcoder problems

```
$ cd ABC
$ acc new abc086
$ cd abc086
  :
$ g++ -O2 -std=c++14 main.cpp
$ oj test
  :
$ acc submit main.cpp
$ acc ..
$ acc add
```

For Python:
```
  :
$ oj test -c 'python main.py'
  :
```

To use more convenient commands, see [atcoder\-cli チュートリアル \| わたしろぐ](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)


### Code Runner setting (VS Code Extension)
- settings.json
```
{
    "code-runner.runInTerminal": true,
    "code-runner.executorMap": {
        "cpp": "cd $dir && g++ -O2 -std=c++14 $fileName && oj test",
        "python": "cd $dir && oj test -c 'python $fileName'"
    },
    "code-runner.respectShebang": false,
    "code-runner.saveFileBeforeRun": true
}
```
then press `Ctrl-Alt-N` keys to run the above command.

## References

### online-judge-tools
- [競技プログラミングのための補助ツールを作った \- うさぎ小屋](https://kimiyuki.net/blog/2017/01/19/pr-online-judge-tools/)
- [kmyk/online\-judge\-tools: Tools for online judge services\. Downloading sample cases, Testing/Submitting your code, and various utilities\.](https://github.com/kmyk/online-judge-tools)

### atcoder-cli
- [コマンドラインツールatcoder\-cliを公開しました \| わたしろぐ](http://tatamo.81.la/blog/2018/12/07/atcoder-cli/)
- [atcoder\-cli チュートリアル \| わたしろぐ](http://tatamo.81.la/blog/2018/12/07/atcoder-cli-tutorial/)

### Problems
- [AtCoder に登録したら次にやること ～ これだけ解けば十分闘える！過去問精選 10 問 ～ - Qiita](https://qiita.com/drken/items/fd4e5e3630d0f5859067)
