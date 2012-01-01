module MCollective
    module Agent
        class Ctjava<RPC::Agent
	    metadata:name        => "SimpleRPC Java App Agent",
                    :description => "Agent to manage Java Apps",
                    :author      => "R.T.Nair",
                    :license     => "ASL2",
                    :version     => "1.0",
                    :url         => "http://kermit.cleartrip.com",
                    :timeout     => 200

            action "start" do
                validate :appname, String
		$app = request.data[:appname]
		run("/etc/init.d/javatest start #{$app}", :stdout => :status, :stderr => :msg)
		reply[:status]
            end
            action "stop" do
                validate :appname, String
		$app = request.data[:appname]
		run("/etc/init.d/javatest stop #{$app}", :stdout => :status, :stderr => :msg)
		reply[:status]
            end
            action "status" do
                validate :appname, String
		$app = request.data[:appname]
		run("/etc/init.d/javatest status #{$app}", :stdout => :status, :stderr => :msg)
		reply[:status]
            end
        end
    end
end

