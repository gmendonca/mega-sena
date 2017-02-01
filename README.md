# mega-sena

Lottery data analysis based on the Brazilian's Lottery [Mega Sena](http://loterias.caixa.gov.br/wps/portal/loterias/landing/megasena/). I tried to make it generic as possible. However I'm still depending on the file provided by Mega Sena about past draws to get to some conclusions. I'm also using the implementation provided in this [article](http://jaguar.fcav.unesp.br/RME/fasciculos/v31/v31_n4/A7_RGiarelli.pdf), to get some insights. It still need a lot of improvements, however it can be used at least for checking if the number was already draw and some other statistics. The `MEGA_SENA` file provided is not always updated, so if you want the newest possible, download from the website.

## TODOs

- Chance of winning doesn't consider all sequences when choosing more than `max_guess`
- Chance of winning is not well built. It need better calculations. Eg.: Consider the expected draws and actual draws using the color lottery theory described in the article.
- Machine Learning

## Requirements

You need Python and pip. Then, you can install the requirements with:
```
pip install -r requirements.txt
```

## Running

```
Usage: python process.py [OPTIONS]
Tries to get a better chance of winning mega sena.
   -f, --file                     Mega Sena file name
   -q, --quantity                 The total of numbers available to be draw, defaults to 60
   -m, --max                      Total of draw numbers, defaults to 6.
   -h, --howmany                  Number of possible 6 numbers to be draw with higher probability
```

## Examples

```
$ python process.py -f "MEGA_SENA" 12 34 45 53 55 58
========> Number never draw before!
+---------------------------------------+------------------------------------------------------------+
|              Description              |                           Value                            |
+---------------------------------------+------------------------------------------------------------+
|               Sequencia               |                  [12, 34, 45, 53, 55, 58]                  |
|  Probability getting 6 correct (1 in) |                          50063860                          |
|  Probability getting 5 correct (1 in) |                           154518                           |
|  Probability getting 4 correct (1 in) |                            2332                            |
|              Sequence sum             |                            257                             |
|        Probability of number 12       |                           9.92%                            |
|        Probability of number 34       |                           10.24%                           |
|        Probability of number 45       |                           9.76%                            |
|        Probability of number 53       |                           11.56%                           |
|        Probability of number 55       |                           8.55%                            |
|        Probability of number 58       |                           9.82%                            |
|        Total number of drawings       |                            1895                            |
| Total number of drawings with winners |                            452                             |
|            Number of draws            |                             5                              |
|                Template               | ('green', 'ivory', 'ivory', 'ivory', 'light_blue', 'pink') |
|              Probability              |                           23.97%                           |
|        Number of expected draws       |                             4                              |
|         Number of combinations        |                           120000                           |
|              Average sum              |                            257                             |
|            Template number            |                            347                             |
+---------------------------------------+------------------------------------------------------------+
========> Sua chance de ganhar: 0.0000048079%
--- Total 0.00410604476929 seconds ---
```

```
$ python process.py -f "MEGA_SENA"
========> Number never draw before!
+---------------------------------------+------------------------------------------------------------+
|              Description              |                           Value                            |
+---------------------------------------+------------------------------------------------------------+
|                Sequence               |                   [1, 5, 19, 20, 41, 45]                   |
|  Probability getting 6 correct (1 in) |                          50063860                          |
|  Probability getting 5 correct (1 in) |                           154518                           |
|  Probability getting 4 correct (1 in) |                            2332                            |
|              Sequence sum             |                            131                             |
|        Probability of number 1        |                           10.08%                           |
|        Probability of number 5        |                           11.77%                           |
|        Probability of number 19       |                           9.29%                            |
|        Probability of number 20       |                           9.39%                            |
|        Probability of number 41       |                           10.82%                           |
|        Probability of number 45       |                           9.76%                            |
|        Total number of drawings       |                            1895                            |
| Total number of drawings with winners |                            452                             |
|            Number of draws            |                             6                              |
|                Template               | ('gray', 'light_blue', 'pink', 'pink', 'yellow', 'yellow') |
|              Probability              |                           32.36%                           |
|        Number of expected draws       |                             6                              |
|         Number of combinations        |                           162000                           |
|              Average sum              |                            138                             |
|            Template number            |                            122                             |
+---------------------------------------+------------------------------------------------------------+
========> Sua chance de ganhar: 0.0000054920%
--- Total 0.00329184532166 seconds ---
```

```
$ python process.py -f "MEGA_SENA" -m 7
========> Number never draw before!
+---------------------------------------+-----------------------------+
|              Description              |            Value            |
+---------------------------------------+-----------------------------+
|                Sequence               | [1, 14, 26, 29, 51, 52, 59] |
|  Probability getting 6 correct (1 in) |          386206920          |
|  Probability getting 5 correct (1 in) |            346996           |
|  Probability getting 4 correct (1 in) |             8007            |
|              Sequence sum             |             232             |
|        Probability of number 1        |            10.08%           |
|        Probability of number 14       |            9.08%            |
|        Probability of number 26       |            8.23%            |
|        Probability of number 29       |            10.29%           |
|        Probability of number 51       |            11.35%           |
|        Probability of number 52       |            10.34%           |
|        Probability of number 59       |            9.87%            |
|        Total number of drawings       |             1895            |
| Total number of drawings with winners |             452             |
+---------------------------------------+-----------------------------+
========> Chance of winning: 0.0000003150%
--- Total 0.0459048748016 seconds ---
```

## Contributing

The project doesn't have the intention of keep growing, it was done for some practice and out of curiosity. Feel free to fork and use it as you pleased. If you really think you have something to add, please provided a Pull Request out of you forked branch.
