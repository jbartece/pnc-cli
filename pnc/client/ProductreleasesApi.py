#!/usr/bin/env python
"""
ProductreleasesApi.py
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


class ProductreleasesApi(object):

    def __init__(self, apiClient):
      self.apiClient = apiClient

    
    def getAll(self, **kwargs):
        """Gets all Product Releases

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
        Returns: 
        """

        allParams = ['pageIndex', 'pageSize', 'sort', 'q']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAll" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/product-releases'
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
        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getAllByProductVersionId(self, **kwargs):
        """Gets all Product Releases of the Specified Product Version

        Args:
            
            pageIndex, int: Page index (required)
            
            pageSize, int: Pagination size (required)
            
            sort, str: Sorting RSQL (required)
            
            q, str: RSQL query (required)
            
            versionId, int: Product Version id (required)
            
        Returns: 
        """

        allParams = ['pageIndex', 'pageSize', 'sort', 'q', 'versionId']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllByProductVersionId" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/product-releases/product-versions/{versionId}'
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
        

        

        
        if ('versionId' in params):
            replacement = str(self.apiClient.toPathValue(params['versionId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'versionId' + '}',
                                                replacement)
        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def createNew(self, **kwargs):
        """Creates a new Product Release

        Args:
            
            versionId, int: Product Version id (required)
            
            body, ProductRelease:  (required)
            
        Returns: 
        """

        allParams = ['versionId', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method createNew" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/product-releases/product-versions/{versionId}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'POST'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
        if ('versionId' in params):
            replacement = str(self.apiClient.toPathValue(params['versionId']))
            replacement = urllib.quote(replacement)
            resourcePath = resourcePath.replace('{' + 'versionId' + '}',
                                                replacement)
        

        

        
        if ('body' in params):
            bodyParam = params['body']
        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getAllSupportLevel(self, **kwargs):
        """Gets all Product Releases Support Level

        Args:
            
        Returns: 
        """

        allParams = []

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getAllSupportLevel" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/product-releases/support-level'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        

        

        

        postData = (formParams if formParams else bodyParam)

        response = self.apiClient.callAPI(resourcePath, method, queryParams,
                                          postData, headerParams, files=files)
	return response

   
    def getSpecific(self, **kwargs):
        """Gets specific Product Release

        Args:
            
            id, int: Product Release id (required)
            
        Returns: 
        """

        allParams = ['id']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method getSpecific" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/product-releases/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'GET'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
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
        """Updates an existing Product Release

        Args:
            
            id, int: Product Release id (required)
            
            body, ProductRelease:  (required)
            
        Returns: 
        """

        allParams = ['id', 'body']

        params = locals()
        for (key, val) in params['kwargs'].iteritems():
            if key not in allParams:
                raise TypeError("Got an unexpected keyword argument '%s' to method update" % key)
            params[key] = val
        del params['kwargs']

        resourcePath = '/product-releases/{id}'
        resourcePath = resourcePath.replace('{format}', 'json')
        method = 'PUT'

        queryParams = {}
        headerParams = {}
        formParams = {}
        files = {}
        bodyParam = None

        

        

        
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

   
