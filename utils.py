from py_boost.gpu.losses import Loss, Metric
import cupy as cp

class PseudoHuberLoss(Loss):
    def __init__(self, delta):
        self.delta = delta
    
    def preprocess_input(self, y_true):
        return y_true
    
    def postprocess_output(self, y_pred):
        return y_pred
    
    def get_grad_hess(self, y_true, y_pred):
        a = y_true - y_pred
        size = a.shape
        sqr = cp.square(a/self.delta)
        ones_arr = cp.ones(size, dtype=cp.float32)
        sqrtp1 = cp.sqrt(ones_arr + sqr)
        N = 1

        grad = -a/sqrtp1/N
        hess = (ones_arr - sqr/(ones_arr + sqr))/sqrtp1/N
        
        return grad, hess

    def base_score(self, y_true):
        return y_true.mean(axis=0)
    
class CustomMSLELoss(Loss):
    """Custom MSLE Implementation"""
    
    def preprocess_input(self, y_true):
        """
        This method defines, how raw target should be processed before the train starts
        We expect y_true has shape (n_samples, n_outputs)
        
        Here we will not do the actual preprocess, but just check if targets are non negative
        
        At that stage y_true is already in GPU memory, so we use CuPy to handle it.
        Usage is the same as NumPy, just replace np with cp
        
        Note: All metrics and losses will be computed with this preprocess target
        """
        assert (y_true >= 0).all()
        return y_true
    
    def postprocess_output(self, y_pred):
        """
        Since we modify the target variable, we also need method, that defines 
        how to process model prediction
        """
        
        return cp.expm1(y_pred)
    
    def get_grad_hess(self, y_true, y_pred):
        """
        This method defines how to calculate gradients and hessians for given loss
        Note that training also supports sample_weight, but its applied outside the loss fn,
        so we don't need to handle it here
        """ 
        # grad should have the same shape as y_pred
        grad = y_pred - cp.log1p(y_true)
        # NOTE: Input could be a matrix in multioutput case!
        # But anyway - hessians are ones for all of them
        # So, we just create (n_samples, 1) array of ones 
        # and after that is will be broadcasted over all outputs
        # grad should have the same shape as y_pred or (n_samples, 1)
        hess = cp.ones((y_true.shape[0], 1), dtype=cp.float32)
        
        return grad, hess

    def base_score(self, y_true):
        """
        One last thing we require to define is base score
        This method defines how to initialize an empty ensemble
        In simplies case it could be just an array of zeros
        But usualy it is better to boost from mean values
        Output shape should be (n_outputs, ) 
        
        Note: y_true is already processed array here
        
        """
        return cp.log1p(y_true).mean(axis=0)
    
class CustomMAELoss(Loss):
    """Custom MAE Implementation"""
    
    def preprocess_input(self, y_true):
        return y_true
    
    def postprocess_output(self, y_pred):
        return y_pred
    
    def get_grad_hess(self, y_true, y_pred):
        grad = cp.sign(y_pred-y_true)
   
        hess = cp.ones((y_true.shape[0], 1), dtype=cp.float32)
        
        return grad, hess

    def base_score(self, y_true):

        return y_true.mean(axis=0)
    
class CustomLogCoshLoss(Loss):
    def preprocess_input(self, y_true):
        return y_true
    
    def postprocess_output(self, y_pred):
        return y_pred
    
    def get_grad_hess(self, y_true, y_pred):
        grad = cp.tanh(y_pred - y_true)
        hess = 4/cp.square(cp.exp(y_pred - y_true) + cp.exp(-y_pred + y_true))

        return grad, hess

    def base_score(self, y_true):
        return y_true.mean(axis=0)
    
class CustomHuberLoss(Loss):
    def __init__(self, delta):
        self.delta = delta
    
    def preprocess_input(self, y_true):
        # assert (y_true >= 0).all()
        return y_true
    
    def postprocess_output(self, y_pred):
        return y_pred
    
    def get_grad_hess(self, y_true, y_pred):
        mask_inner = cp.absolute(y_true - y_pred) < self.delta
        mask_outer = cp.invert(mask_inner)
        grad = mask_inner * (y_pred - y_true) + mask_outer * cp.sign(y_pred - y_true) * self.delta
        hess = mask_inner * cp.ones((y_true.shape[0], 1), dtype=cp.float32) + mask_outer * cp.zeros((y_true.shape[0], 1), dtype=cp.float32)
        
        return grad, hess

    def base_score(self, y_true):
        return y_true.mean(axis=0)
    
class CustomMAEMetric(Metric):
    """First, let's define eval metric to estimate model quality while training"""
    
    def error(self, y_true, y_pred):
        return cp.abs(y_true - y_pred)
    
    def compare(self, v0 ,v1):
        """
        The last required method is .compare
        It should return True if v0 metric value is better than v1, False othewise
        """
        return v0 < v1