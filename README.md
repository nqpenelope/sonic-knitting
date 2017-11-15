# sonic-knitting

Sonic-knitting is an audio interpretation of a knitting pattern. Knitting patterns are essentially algorithms, and a simple rotation algorithm was used to imitate a spiraling knitted cowl using Python. NumPy was employed to generate matrices representing the rows of the pattern. To imitate the act of knitting, the rows were transposed to columns, with the first sound entering alone as the first stitches are knit. As rows are worked, the piece increases in size, and the vertical complexity of the transposition becomes apparent.

Each tone represents a single stitch. Low tone represents knit stitches; higher tone represents purl stitches. The pattern consists 63 cast-on stitches, with a basic k8p8 rib then worked in the round.

[jenny-bower.com/sonic-knitting](http://jenny-bower.com/sonic-knitting)