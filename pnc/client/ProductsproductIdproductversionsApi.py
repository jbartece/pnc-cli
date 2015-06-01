#!/usr/bin/env python
"""
ProductsproductIdproductversionsApi.py
Copyright 2015 Reverb Technologies, Inc.

   Licensed under the Apache License, Version 2.0 (the "License");
   you may not use this file except in compliance with the License.
   You may obtain a copy of the License at

       http://www.apache.org/licenses/LICENSE-2.0

   Unless required by applicable law or agreed to in writing, software
   distributed under the License is distributed on an "AS IS" BASIS,
   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
   See the License for the specific language governing permissions and
   limitations under the License.

NOTE: This class is auto generated by the swagger code generator program. Do not edit the class manually.
"""
import sys
import os
import urllib

from models import *


class ProductsproductIdproductversionsApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def getAll(self, **kwargs):
        """Gets all Product Versions

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
            productId, int: Product id (required)
            
        Returns: 
        """

        allParams = ['pageIndex', 'pageSize', 'sort', 'q', 'productId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAll" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/products/{productId}/product-versions'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        
        if ('pageIndex' in params):
            queryParams['pageIndex'] = self.apiClient.toPathValue(params['pageIndex'])
        
        if ('pageSize' in params):
            queryParams['pageSize'] = self.apiClient.toPathValue(params['pageSize'])
        
        if ('sort' in params):
            queryParams['sort'] = self.apiClient.toPathValue(params['sort'])
        
        if ('q' in params):
            queryParams['q'] = self.apiClient.toPathValue(params['q'])
        

        

        
        if ('productId' in params):
            replacement = str(self.apiClient.toPathValue(params['productId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'productId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def createNew(self, **kwargs):
        """Creates a new Product Version

        Args:
            
            productId, int: Product id (required)
            
            body, ProductVersion:  (required)
            
        Returns: 
        """

        allParams = ['productId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createNew" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/products/{productId}/product-versions'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
        if ('productId' in params):
            replacement = str(self.apiClient.toPathValue(params['productId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'productId' + '}',
                                                replacement)
        

        

        
        if ('body' in params):
            bodyParam = params['body']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getSpecific(self, **kwargs):
        """Gets specific Product Version

        Args:
            
            productId, int: Product id (required)
            
            id, int: Product Version id (required)
            
        Returns: 
        """

        allParams = ['productId', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSpecific" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/products/{productId}/product-versions/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
        if ('productId' in params):
            replacement = str(self.apiClient.toPathValue(params['productId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'productId' + '}',
                                                replacement)
        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def update(self, **kwargs):
        """Updates an existing Product Version

        Args:
            
            productId, int: Product id (required)
            
            id, int: Product Version id (required)
            
            body, ProductVersion:  (required)
            
        Returns: 
        """

        allParams = ['productId', 'id', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/products/{productId}/product-versions/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
        if ('productId' in params):
            replacement = str(self.apiClient.toPathValue(params['productId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'productId' + '}',
                                                replacement)
        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        

        

        
        if ('body' in params):
            bodyParam = params['body']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getBuildConfigurationSets(self, **kwargs):
        """Gets build configuration sets associated with a product version

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
            productId, int: Product id (required)
            
            id, int: Product Version id (required)
            
        Returns: 
        """

        allParams = ['pageIndex', 'pageSize', 'sort', 'q', 'productId', 'id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getBuildConfigurationSets" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/products/{productId}/product-versions/{id}/build-configuration-sets'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        
        if ('pageIndex' in params):
            queryParams['pageIndex'] = self.apiClient.toPathValue(params['pageIndex'])
        
        if ('pageSize' in params):
            queryParams['pageSize'] = self.apiClient.toPathValue(params['pageSize'])
        
        if ('sort' in params):
            queryParams['sort'] = self.apiClient.toPathValue(params['sort'])
        
        if ('q' in params):
            queryParams['q'] = self.apiClient.toPathValue(params['q'])
        

        

        
        if ('productId' in params):
            replacement = str(self.apiClient.toPathValue(params['productId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'productId' + '}',
                                                replacement)
        
        if ('id' in params):
            replacement = str(self.apiClient.toPathValue(params['id']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'id' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
