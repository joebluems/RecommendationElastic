# RecommendationElastic
Deploy a Recommendation Engine in ElasticSearch based on GroupLens movie data

Requires Mahout and Elasticsearch running in standalone mode - will also work on a Hadoop cluster.

1. Raw Data

  <b>u.item </b> - movie metadata for 1,682 films (pipe-delimited)

  <b>u.data </b>- user/item ratings (tab-delimited)


2. Create the files for indexing

  <b>python metaData.py > index.json </b> (python script to read items and writes JSON for bulk load)

  <b>./genLogLikelihood </b> (this runs a Mahout job and writes similar items to output/part-r-00000

  <b>python indicators.py > update.json </b> (python script reads mahout output and writes JSON for bulk update)


3. Create and load the index

   <b>bin/elasticsearch</b> (start Elasticsearch)
   
   <b>curl -XPUT 'localhost:9200/movie'; echo</b> (create index)
   
   <b>curl -s -XPOST localhost:9200/_bulk --data-binary @index.json; echo </b> (bulk load metadata)
   
   <b>curl -s -XPOST localhost:9200/_bulk --data-binary @update.json; echo</b> (bulk update indicators)
   
   
4. Query the search engine
  
  <b>./qSearch</b> (search titles for the token "hunt")

  <b>./qRecommend</b> (get recommendations for ids 265 474 and 180)
  
  <b>./qRandom</b> (get recommendations for ids, randomize results - rerun for different results)
  
