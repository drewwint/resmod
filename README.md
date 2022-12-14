# resmod: a package for creating orthogonalized interaction terms by centering residuals

## What is resmod? 
**resmod** is a Python package that provides the ability to quickly create orthogonalized interaction terms by centering residuals. This approach to testing interaction prevents the user from violating basic assumptions of regression -- specificaly that there should be no correlated residuals. Because the interaction term is orthogonalized from the model, you are able to interpret both direct effects and interaction terms in the same model. Not only is this convienient but it reduces the number of test run on your data. 

This approach is based on the work of Todd Little. 
See the citation: Little, T. D., Card, N. A., Bovaird, J. A., Preacher, K. J., & Crandall, C. S. (2007). Structural equation modeling of mediation and moderation with contextual factors. Modeling contextual effects in longitudinal studies, 1, 207-230.

### Functions
- **residual_center** 
	- Two-way orthogonalized interaction that can be use in any regression-based model
- **three_center** 
	- Three-way orthogonalized interaction that can be used in any regression-based model
- **orthogonalize** 
	- Multiple orthogonalized interactions to be used in latent SEM interaction modeling


### Installation

```
# git
git clone https://github.com/drewwint/resmod.git
cd resmod
pip install . 

```

```
# PyPi
pip install resmod

```

### Dependencies
- [NumPy](https://www.numpy.org)
- [pandas](https://pandas.pydata.org)
- [statsmodels](https://www.statsmodels.org)

### Usage 

```
# residual_center: Orthogonalizing single two-way interaction from Ducan data
  ## Packages
    from resmod.single import residual_center         # for orthogonalizing 
    import statsmodels.formula.api as smf             # for estimation 
    import statsmodels as sms             
    from statsmodels import datasets                  # for importing data
    import numpy as np                                # for data structring
    import pandas as pd                               # for dataframe 
    
  ## Getting data
    duncan_prestige = sms.datasets.get_rdataset("Duncan", "carData")
    income = duncan_prestige.data.income
    education = duncan_prestige.data.education
    
  ## Creating dataframe
    v1 = np.array(income)                             # ensure v1 is an array
    v2 = np.array(education)                          # ensure v2 is an array 
    dat = pd.DataFrame({"income": v1, "education" : v2})
  
  ## Estimation 
    residual_center(dat.income, dat.education)
  
  ## Returns
    #array([ 63.11264837,    229.8491846,    741.28285426,  -191.61545996,  143.13497759, 
    #       -1522.02012271,  250.49755451,   1222.03876523,  281.50598242,  463.22429449,  
    #       -657.16077574,   951.3190848 ,   923.98157381,  -761.79683046, -500.35610126,  
    #       -798.28161848,  -474.82578368,  -357.03501052,  -457.2861054 ,  585.94123821,
    #       -981.98093767,  -476.50649685,  -312.02816875,  -549.40617942,  165.39170698,  
    #       -458.91783728,  -1052.25086135, -293.40322494,   169.06536061, -372.67648496,   
    #        101.34978524,   1153.8352266,  -337.3613032,    599.90768769,  386.69161908,   
    #        248.37917402,   182.34841689,   117.02343887,   679.23266571,  360.97604371,
    #        115.6538024,    194.02207051,   612.22286945,  -485.36288933,  98.28416593]
    #        )
```

```
# orthogonalize: Orthogonalizing two list of variables from Duncan data
   ### Output could be used for multiple orthogonalized interactions or
   ### to create interactions of all observed variables to be used in a latent interaction

 ## Packages
      from resmod.sem import orthogonalize
      import statsmodels.formula.api as smf
      import statsmodels as sms
      from statsmodels import datasets
      import numpy as np
      import pandas as pd

 ## Getting data
      duncan_prestige = sms.datasets.get_rdataset("Duncan", "carData")
      income = duncan_prestige.data.income
      education = duncan_prestige.data.education

 ## Creating dataframe
      income = np.array(duncan_prestige.data.income)
      education = np.array(duncan_prestige.data.education)
      prestige = np.array(duncan_prestige.data.prestige)
      dat = pd.DataFrame({"income": income, "education": education, "prestige": prestige})

 ## Creating lists of column names for interactions 
    ## You could include any number variables in each list for your purposes 
      l1 = ["income"]
      l2 = ["education", "prestige"]


 ## Estimation
      r = orthogonalize(l1, l2, dat)
      r.head()

 ## Returns 
   # Dataframe
   #     income.education  income.prestige
   #  0         63.112648        34.246807
   #  1        229.849185       399.315757
   #  2        741.282854       732.789351
   #  3       -191.615460      -277.473163
   #  4        143.134978       276.041595

```

### Comparative testing
In addition to each functions testing files, we replicated results from functions in r packages including:
- [rockchalk](https://cran.r-project.org/web/packages/rockchalk/rockchalk.pdf)
- [semTools](https://cran.r-project.org/web/packages/semTools/semTools.pdf)

### Contributing to resmod

All contributions, bug reports, bug fixes, documentation improvements, enhancements, and ideas are welcome.

