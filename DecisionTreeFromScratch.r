library(tidyverse)

# Set Up
df <- iris
df[,5] <- as.numeric(df[,5])
ind <- sample(seq_len(nrow(df)), size = smp_size)
tr <- df[ind,]
ts <- df[-ind,]
max_depth <- 3

# Gini
gini <- function(df, x_ind, y_ind, val){
    g <- 0

    l <- df[,c(x_ind,y_ind)] %>%
        filter(df[,x_ind]>=val) %>%
        group_by(cat=.[[2]]) %>%
        summarize(count=n()) %>%
        as.data.frame

    ln <- colSums(l)[["count"]]

    r <- df[,c(x_ind,y_ind)] %>%
        filter(df[,x_ind]<val) %>%
        group_by(cat=.[[2]]) %>%
        summarize(count=n()) %>%
        as.data.frame
    
    rn <- colSums(r)[["count"]]

    l_gini <- l$count %>%
        map(~ (./ln)**2) %>%
        as.numeric() %>%
        sum()

    r_gini <- r$count %>%
        map(~ (./rn)**2) %>%
        as.numeric() %>%
        sum()

    return((ln * (1-l_gini) + rn * (1-r_gini))/nrow(df))
}

# Search Minimum Gini
searchMinGini <- function(df, x_inds, y_ind, depth){{
        if(depth>=max_depth){
            cls <- names(sort(table(df[,y_ind]), decreasing = TRUE))[1]
            cat(sprintf("Depth: %d, Class: %s \n", depth,cls))
            return("Success")
        } else{
            gmin <- 1.00
            imin <- NULL
            xmin <- NULL

            for(x_ind in x_inds){
                for(i in 1:nrow(df)){
                    g <- gini(df, x_ind, y_ind, df[i,x_ind])
                    if(g < gmin){
                        gmin <- g
                        imin <- i
                        xmin <- x_ind
                    }
                }
            }

            l_df <- df %>%
                filter(df[,xmin]>=df[i,xmin])
            r_df <- df %>%
                filter(df[,xmin]<df[i,xmin])

            cat(sprintf("Depth: %d, Separation at: %s = %f\n", depth, names(df)[xmin], df[i,xmin]))

            searchMinGini(l_df,x_inds,y_ind,depth+1)
            searchMinGini(r_df,x_inds,y_ind,depth+1)
        }
    }
}
